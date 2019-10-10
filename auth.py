from __future__ import print_function
import os

home = os.environ['HOME']


def get_authority(authority, authdir=home + '/.auth/', strip=True):
    """
    Read the authentication stored in a a hidden file so that it is not embedded in code

    Parameters
        authority: What authority file to read
        authdir:    Directory for authentication file, defaults to ~/.auth

    Return
        auth_session:   token/password from file
    """

    keyfile = authdir + authority

    try:
        with open(keyfile) as f:
            auth_session = f.read()
    except Exception as exc:
        print('get_authority: error reading {}'.format(keyfile))
        raise exc

    if strip:
        auth_session = auth_session.strip()
        
    return auth_session
