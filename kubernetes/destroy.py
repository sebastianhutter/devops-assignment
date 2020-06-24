#!/usr/bin/env python

"""
    remove the given digitalocean kubernetes cluster
"""

from dotenv import load_dotenv, find_dotenv
import os
import sys
import requests
import time
import json

class DigitalOceanClient(object):
    def __init__(self, token):
        super().__init__()

        self.token = token
        self.request_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }
        self.base_url = 'https://api.digitalocean.com/v2'

        # cluster id of freshly deployed cluster
        self.k8s_cluster_id = None

        # test authentication by getting account info
        r = requests.get('{}/account'.format(self.base_url), headers=self.request_headers)
        r.raise_for_status()

    def get_cluster_id(self, name):
        """
            get the cluster id of the specified cluster
        """
        r = requests.get('{}/kubernetes/clusters'.format(self.base_url), headers=self.request_headers)
        r.raise_for_status()
        response_body = r.json()

        for c in response_body['kubernetes_clusters']:
            if c['name'] == name:
                self.k8s_cluster_id = c['id']


    def delete_cluster(self):
        if self.k8s_cluster_id:
            r = requests.delete(
                '{}/kubernetes/clusters/{}'.format(self.base_url, self.k8s_cluster_id), 
                headers=self.request_headers
            )
            r.raise_for_status()

if __name__ == "__main__":
    try:
        print("Load application config")
        # load configuration values from .env
        load_dotenv(find_dotenv())

        # configure application
        DO_TOKEN = os.getenv("DIGITALOCEAN_ACCESS_TOKEN")
        CLUSTER_NAME = os.getenv("CLUSTER_NAME", 'homework1')

        if not DO_TOKEN:
            raise ValueError("Digitalocean Access token not specified.")

        # initialize digitalocean client
        print("Initialize client")
        do = DigitalOceanClient(DO_TOKEN)

        # delete cluster
        print("Delete cluster")
        do.get_cluster_id(CLUSTER_NAME)
        do.delete_cluster()

    except:
        e = sys.exc_info()
        print(e)
        sys.exit(1)

    
