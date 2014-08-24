import data

print("""<!DOCTYPE htm>
<html>
  <head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="visualisation.css"/>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <title>Viewport visualisation</title>
  </head>
  <body>

<div class="legend">
  <h1>Viewport sizes</h1>
  <div class="legend_scale">
    <div class="legend_scale_vertical"></div><div class="legend_scale_horizontal"></div><div class="legend_scale_vertical"></div>
  </div>
  320px
</div>
""")

items = data.viewports

for item in items:
    count = items[item]
    style = (
        int(round(item[0] / 10.0)),
        int(round(item[1] / 10.0)),
        min(count / 10.0, 1)
    )
    print('<div class="box" style="width:%s;height:%s;opacity:%s"></div>' % style)
print("""  </body>
</html>""")
