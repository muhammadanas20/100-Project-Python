# Day 26: Secure User Profile App

Store profile details while hashing the password with a unique salt.

## Concepts

- getpass
- PBKDF2
- salts
- JSON storage

## Setup

Create and activate a virtual environment, then continue below.

This project uses only the Python standard library.

## Run

    python secure_profile.py

Expected result: A profile is saved without storing the original password.

## Extension challenge

Add a verify_password() function.

## Classroom boundary

This demonstrates hashing basics; production authentication needs a reviewed identity system, rate limiting, secure sessions, and careful secret management.
