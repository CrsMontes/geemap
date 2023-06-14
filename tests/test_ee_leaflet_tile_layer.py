"""Tests for `test_ee_leaflet_tile_layer` package."""

import unittest
from unittest.mock import patch

import ee

import fake_ee
from geemap import ee_leaflet_tile_layer


@patch.object(ee, "Feature", fake_ee.Feature)
@patch.object(ee, "Image", fake_ee.Image)
class TestEeLeafletTileLayer(unittest.TestCase):
    """Tests for `test_ee_leaflet_tile_layer` package."""

    def test_ee_leaflet_tile_layer(self):
        layer = ee_leaflet_tile_layer.EeLeafletTileLayer(
            ee_object=ee.Image(1),
            vis_params={"min": 42, "palette": "012345"},
            name="a-name",
            shown=False,
            opacity=0.5,
        )
        self.assertEqual(layer.vis_params, {"min": 42, "palette": "#012345"})
        self.assertEqual(layer.url_format, "url-format")
