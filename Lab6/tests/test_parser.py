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