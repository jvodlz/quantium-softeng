from app import app


def test_001_header_exist(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#title-header", timeout=8)


def test_002_vis_exist(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#pink-morsel-sales-graph", timeout=8)


def test_003_region_filter_exist(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=8)
