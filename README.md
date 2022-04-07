# Genderly .po checker

This repo contains a small script to check a gettext `.po` file against the [genderly](https://gendern.jetzt) webservice.
It marks all entries for which genderly reports an ungendered word as [`fuzzy`](https://www.gnu.org/software/gettext/manual/html_node/Fuzzy-Entries.html), meaning they need to be looked at again by a translator