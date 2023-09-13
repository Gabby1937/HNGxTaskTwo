# Project Documentation: Simple REST API for CRUD Operations

## Table of Contents

1. Introduction
2. API Overview
3. Database Schema
4. API Endpoints
5. Testing
6. Dynamic Parameter Handling
7. GitHub Repository
8. Documentation
9. Hosting
10. Conclusion

---

## 1. Introduction

Welcome to the documentation for the "Simple REST API for CRUD Operations" project. This project aims to create a RESTful API that performs CRUD (Create, Read, Update, Delete) operations on a resource, specifically a "person." The API interacts with a PostgreSQL database and provides dynamic parameter handling to enable flexibility in working with individuals' records.

---

## 2. API Overview

### Programming Language and Database

The API is built using Python with the Flask web framework and SQLAlchemy for database interactions. It communicates with a PostgreSQL database to store and retrieve "person" records.

### CRUD Operations

The API provides the following CRUD operations:

- **CREATE:** Adding a new person
- **READ:** Fetching details of a person
- **UPDATE:** Modifying details of an existing person
- **DELETE:** Removing a person

All database interactions are designed to be secure and protected against common vulnerabilities such as SQL injection.

---

## 3. Database Schema

The database schema for this project consists of a single table, "Person," with the following columns:

- `id`: An auto-incremented unique identifier for each person.
- `name`: A string representing the name of the person.

The simplicity of the schema allows for easy management of individual records.

---

## 4. API Endpoints

The API exposes the following endpoints:

- **CREATE:** `/api/persons` (HTTP POST)

  - Creates a new person record.
- **READ:** `/api/persons/<int:person_id>` (HTTP GET)

  - Retrieves details of a specific person by their unique ID.
- **UPDATE:** `/api/persons/<int:person_id>` (HTTP PUT)

  - Modifies details of an existing person using their unique ID.
- **DELETE:** `/api/persons/<int:person_id>` (HTTP DELETE)

  - Deletes a person record using their unique ID.

---

## 5. Testing

The project includes unit tests for each CRUD operation. The tests are written using the Python unittest framework and can be executed to ensure the API functions correctly. Testing tools such as Postman or Python scripts using the `requests` library are recommended for thorough testing.

---

## 6. Dynamic Parameter Handling

The API is designed to handle dynamic input. It can process operations using the name of a person as a parameter. For example, if "Mark Essien" is provided as a parameter, all CRUD operations can be performed on the record associated with that name. Additionally, the API performs validation to ensure that only string values are accepted for names; other data types are not allowed.

---

## 7. GitHub Repository

The project is hosted on GitHub, and the repository is well-organized. The repository contains the following components:

- **README.md:** This file provides instructions on setting up, running, and using the API.
- **app.py:** The main application file containing API routes and database configurations.
- **create_tables.py:** A script to create the necessary database tables.
- **tests/task2.py:** Unit tests for the API using the Python unittest framework.
- **UML Diagrams:** Unified Modeling Language (UML) diagrams representing the project's structure and relationships.

---

## 8. Documentation

Project documentation is provided to assist users in understanding and using the API effectively. The documentation is available in the repository as a separate file named "DOCUMENTATION.md." It includes:

- Standard formats for requests and responses for each API endpoint.
- Sample usage of the API, including example requests and expected responses.
- Any known limitations or assumptions made during development.
- Instructions for setting up and deploying the API locally or on a server.

---

## 9. Hosting

The API can be hosted on a server for remote accessibility. Hosted endpoints should follow a URL structure like `https://yourdomain.com/api`. It is essential to test the hosted API extensively using various testing tools to ensure its accessibility before production use.

---

## 10. Conclusion

This project demonstrates the development of a simple yet effective REST API for CRUD operations on a "person" resource. It emphasizes security, flexibility, and thorough testing. The clear documentation and GitHub repository organization make it easy for developers to understand, use, and extend the API for their specific needs.

Thank you for considering this project, and I hope it serves as a valuable resource for your REST API development endeavors.

---
