from parser import parse_product_basic, parse_availability


def test_parse_product_basic_extracts_id(valid_product):
    response = valid_product
    result = parse_product_basic(response)
    assert result["id"] == response["id"]


def test_parse_product_basic_extracts_name(valid_product):
    response = valid_product
    result = parse_product_basic(response)
    assert result["name"] == response["name"]


def test_parse_product_basic_returns_only_id_and_name(valid_product):
    response = valid_product
    result = parse_product_basic(response)
    assert set(result.keys()) == {"id", "name"}
    assert "in_stock" not in result

def test_parse_availability_when_in_stock(valid_product):
    response = valid_product
    result = parse_availability(response)
    assert result is True

def test_parse_availability_when_out_of_stock(product_out_of_stock):
    response = product_out_of_stock
    result = parse_availability(response)
    assert result is False


def test_parse_availability_when_field_missing(minimal_product):
    response = minimal_product
    result = parse_availability(response)
    assert result is False