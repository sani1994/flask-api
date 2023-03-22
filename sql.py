"""
write all sql query string's here
"""

get_dest_sql = "SELECT code FROM ports WHERE parent_slug='{destination}'"

get_price_sql = "SELECT day, AVG(price),COUNT(price) FROM prices where orig_code='{origin}' and" \
                " dest_code='{destination_code}' and day between '{date_from}' and '{date_to}' group by day"

get_code_from_region_slug_sql = "select code from ports full outer join regions on ports.parent_slug=regions.parent_slug " \
                                "where regions.slug='{region_slug}' or regions.parent_slug='{region_slug}' " \
                                "or ports.parent_slug='{region_slug}'"
