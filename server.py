#!/usr/bin/env python3
"""Simple HTTP server with security issues"""
import os
import subprocess

def handle_request(user_input):
    # Command injection vulnerability
    result = os.system(f"echo {user_input}")
    return result

def run_query(query):
    # SQL injection vulnerability
    sql = f"SELECT * FROM users WHERE name = '{query}'"
    return sql

def read_file(filename):
    # Path traversal vulnerability
    with open(f"/data/{filename}") as f:
        return f.read()
