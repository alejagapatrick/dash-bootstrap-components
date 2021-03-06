from pathlib import Path

import dash_html_components as html

from ...api_doc import ApiDoc
from ...helpers import (
    ExampleContainer,
    HighlightedSource,
    load_source_with_environment,
)
from ...metadata import get_component_metadata

HERE = Path(__file__).parent

popover_source = (HERE / "popover.py").read_text()


def get_content(app):
    return [
        html.H2("Popover"),
        ExampleContainer(
            load_source_with_environment(
                popover_source, "popover", {"app": app}
            )
        ),
        HighlightedSource(popover_source),
        ApiDoc(
            get_component_metadata("src/components/Popover.js"),
            component_name="Popover",
        ),
        ApiDoc(
            get_component_metadata("src/components/PopoverHeader.js"),
            component_name="PopoverHeader",
        ),
        ApiDoc(
            get_component_metadata("src/components/PopoverBody.js"),
            component_name="PopoverBody",
        ),
    ]
