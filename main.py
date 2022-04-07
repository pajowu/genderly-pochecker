from email.policy import default
from tabnanny import check
import click
import requests
import polib
import tqdm


@click.command()
@click.argument("po_path")
@click.argument("out")
@click.option("--check-endpoint", default="https://app.gendern.jetzt/check")
@click.option("--tags", default=["fuzzy"], multiple=True)
def check_po_file(po_path, out, check_endpoint, tags):
    po = polib.pofile(po_path)
    matched_count = 0
    for entry in tqdm.tqdm(po):
        text = entry.msgstr
        req = requests.post(check_endpoint, json={"text": text})
        assert req.ok
        if req.json()["matches"]:
            entry.flags.extend(tags)
            matched_count += 1
    po.save(out)
    print(f"Found {matched_count} matching entries.")


if __name__ == "__main__":
    check_po_file()
