
Trimmed_Product = Table.TransformColumns(Previous_Step, {{"Product", Text.Trim, type text}}),
Upper_Product = Table.TransformColumns(Trimmed_Product, {{"Product", Text.Upper, type text}})
