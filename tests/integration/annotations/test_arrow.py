from __future__ import absolute_import

from bokeh.io import save
from bokeh.models import Arrow
from bokeh.plotting import figure
from selenium.webdriver.common.action_chains import ActionChains

import pytest
pytestmark = pytest.mark.integration

HEIGHT = 600
WIDTH = 600

def test_arrow(output_file_url, selenium, screenshot):

    # Have to specify x/y range as labels aren't included in the plot area solver
    plot = figure(height=HEIGHT, width=WIDTH, x_range=(0,10), y_range=(0,10), tools='')

    arrow1 = Arrow(x_start=1, y_start=3, x_end=6, y_end=8,
                   line_color='green', line_alpha=0.7,
                   line_dash='8 4', line_width=5,
                   end_line_width=8)

    arrow2 = Arrow(x_start=2, y_start=2, x_end=7, y_end=7,
                   start_style='normal', end_style='vee',
                   start_fill_color='indigo', end_fill_color='orange',
                   end_size=50)

    plot.add_annotation(arrow1)
    plot.add_annotation(arrow2)

    # Save the plot and start the test
    save(plot)
    selenium.get(output_file_url)

    # Take screenshot
    assert screenshot.is_valid()
