import json
import os.path


LOCAL_PATH = 'tests/resources/'
ITEM_LIMIT = 20


def fixture_path(path):
    return os.path.normpath('{}{}'.format(LOCAL_PATH, path))


def load_json_fixture(path):
    with open(fixture_path(path), 'r') as data_file:
        return json.load(data_file)


def fake_data(url, mocker, altpath=False, include_write_methods=False):
    """Register requests_mock routes using fixture data and paging headers."""
    path_parts = url.split('/')[6:]
    path = '/'.join(path_parts) if altpath is False else altpath
    with open(fixture_path(path), 'r') as data_file:
        data_txt = data_file.read()

    data = json.loads(data_txt)
    data_len = len(data)

    headers = {}
    count = 0
    while True:
        count += 1
        if data_len > ITEM_LIMIT and isinstance(data, list):
            returned_data = data[:ITEM_LIMIT]
            returned_data_txt = json.dumps(returned_data)
            data = data[ITEM_LIMIT:]
            data_txt = json.dumps(data)
            paging_url = url.replace('.json', '/page/{}.json'.format(count))
            _register(
                mocker,
                paging_url.replace(" ", "+"),
                returned_data_txt,
                headers.copy(),
                include_write_methods,
            )
            headers = {'link': '{}; rel="next"'.format(paging_url)}
            data_len = len(data)
        else:
            _register(
                mocker,
                url.replace(" ", "+"),
                data_txt,
                headers.copy(),
                include_write_methods,
            )
            break


def _register(mocker, url, text, headers, include_write_methods):
    mocker.get(url, text=text, headers=headers)
    if include_write_methods:
        mocker.post(url, text=text, headers=headers)
        mocker.put(url, text=text, headers=headers)
