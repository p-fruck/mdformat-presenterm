from collections.abc import Mapping

from markdown_it import MarkdownIt
from mdformat.renderer import DEFAULT_RENDERERS, RenderContext, RenderTreeNode
from mdformat.renderer.typing import Render


def update_mdit(mdit: MarkdownIt) -> None:
    pass


def render_heading(
    node: RenderTreeNode,
    context: RenderContext,
) -> str:
    # Let mdformat do all the normal heading rendering first.
    rendered = DEFAULT_RENDERERS["heading"](node, context)

    # ATX heading: "# foo", "## foo", etc.
    # Don't touch it.
    if node.markup not in ("=", "-"):
        return rendered

    # mdformat's default renderer has converted:
    #
    #     foo
    #     ===
    #
    # into:
    #
    #     # foo
    #
    # or:
    #
    #     foo
    #     ---
    #
    # into:
    #
    #     ## foo
    #
    # Remove the ATX prefix that mdformat just added.
    if node.markup == "=":
        prefix = "# "
    else:
        prefix = "## "

    if not rendered.startswith(prefix):
        return rendered

    heading_text = rendered[len(prefix):]

    # Multi-line rendered heading (e.g. a wrapped long title): underline length
    # would be ambiguous, so leave it as ATX rather than emit a broken Setext.
    if "\n" in heading_text:
        return rendered

    # Setext underline length is not preserved by the parser, so use a fixed
    # length rather than one derived from the heading text length.
    return f"{heading_text}\n{node.markup * 3}"


RENDERERS: Mapping[str, Render] = {
    "heading": render_heading,
}
