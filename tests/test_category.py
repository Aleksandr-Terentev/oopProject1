def test_init_category(category1, product1, product2):
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только"
                                     " коммуникации, "
                                     "но и получения дополнительных"
                                     " функций для удобства жизни")
