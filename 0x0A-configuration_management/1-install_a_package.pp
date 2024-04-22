#!/usr/bin/pup

# This puppet script installs a flask package using pip3

package { 'flask':
    ensure   =>   '2.1.0',
    provider =>   'pip3',
}
