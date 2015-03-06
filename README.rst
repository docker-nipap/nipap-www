Docker image for nipap-www
==========================

Description
----------

Docker container for running nipap-www. Requires an existing and running nipapd 
server. Ideally, this is a docker container such as ``coxley/nipapd``.

.. _coxley/nipapd: https://github.com/docker-nipap/nipapd

Setup
-----

The setup is controlled by passing in environment variables during container
start. This allows for adjustable setup.

Below are the current used variables and their defaults:

+-------------+--------------------------+
| NIPAPD_AUTH | local                    |
+-------------+--------------------------+
| EMAIL_FROM  | nipap@localhost          |
+-------------+--------------------------+
| EMAIL_TO    | you@yourdomain.com       |
+-------------+--------------------------+
| SMTP_SERVER | localhost                |
+-------------+--------------------------+
| NIPAPD      | nipapd                   |
+-------------+--------------------------+
| NIPAPD_USER | ``N/A``                  |
+-------------+--------------------------+
| NIPAPD_PASS | ``N/A``                  |
+-------------+--------------------------+
| DEBUG       | false                    |
+-------------+--------------------------+
| WELCOME_MSG | 'NIPAP Docker Container' |
+-------------+--------------------------+

Most other infortmation on getting the entire environment running is located in
the README for the daemon container linked above. It shows an example of a
fully working setup.
