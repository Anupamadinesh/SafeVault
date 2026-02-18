# SafeVault – Secure ASP.NET Core Web API

## Overview
SafeVault is a secure web application built using ASP.NET Core Web API to demonstrate authentication, authorization, input validation, and protection against common web vulnerabilities.

## Security Vulnerabilities Identified
- SQL Injection via unsafe queries
- Cross-Site Scripting (XSS) through unvalidated input
- Weak authentication without role separation

## Fixes Applied
- Used Entity Framework Core with LINQ to prevent SQL injection
- Implemented DataAnnotations and model validation
- Added JWT-based authentication with role-based access control (RBAC)
- Applied output encoding to prevent XSS

## Role-Based Access Control
- Admin: Access to secure vault endpoints
- User: Limited access

## Testing
- xUnit tests verify authentication
- SQL injection attempts are blocked
- XSS payloads are sanitized

## Copilot Usage
GitHub Copilot was used to:
- Generate secure authentication logic
- Suggest JWT configuration patterns
- Identify unsafe SQL usage and replace it with LINQ
- Assist in writing security-focused unit tests
