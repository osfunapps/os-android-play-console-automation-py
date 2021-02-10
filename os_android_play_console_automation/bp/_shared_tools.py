from os_android_play_console_automation.bp import sample_tools


# will build the service
def build_service(client_secrets_path):
    args = [str(__file__)]

    # Authenticate and construct service.
    service, flags = sample_tools.init(
        args,
        'androidpublisher',
        'v3',
        __doc__,
        client_secrets_path,
        parents=[],
        scope='https://www.googleapis.com/auth/androidpublisher')

    # fix google's shitty algorithm of calculating timeout of the http driver to make sure the apk uploaded successfully
    for key, val in service._http.connections.items():
        val.sock.settimeout(260)

    return service


# will get the edit id from the execute
def get_edit_id(service, package_name):
    edit_request = service.edits().insert(body={}, packageName=package_name)
    result = edit_request.execute()
    return result['id']


# will commit the request to Edit's api
def commit(service, edit_id, package_name):
    commit_request = service.edits().commit(editId=edit_id, packageName=package_name).execute()
    print('Edit "%s" has been committed' % (commit_request['id']))
