using Microsoft.AspNetCore.Mvc;
using SafeVault.Data;
using SafeVault.Models;
using SafeVault.Services;
using System.Security.Cryptography;
using System.Text;

namespace SafeVault.Controllers;

[ApiController]
[Route("api/auth")]
public class AuthController : ControllerBase
{
    private readonly AppDbContext _context;
    private readonly TokenService _tokenService;

    public AuthController(AppDbContext context, TokenService tokenService)
    {
        _context = context;
        _tokenService = tokenService;
    }

    [HttpPost("login")]
    public IActionResult Login([FromBody] LoginRequest request)
    {
        // Input validation check
        if (!ModelState.IsValid)
            return BadRequest("Invalid input data.");

        var hashedPassword = HashPassword(request.Password);

        var user = _context.Users
            .FirstOrDefault(u =>
                u.Username == request.Username &&
                u.PasswordHash == hashedPassword);

        if (user == null)
            return Unauthorized("Invalid username or password.");

        var token = _tokenService.CreateToken(user);

        return Ok(new
        {
            message = "Login successful",
            token = token
        });
    }

    // Secure password hashing using SHA256
    private static string HashPassword(string password)
    {
        using var sha = SHA256.Create();
        var bytes = sha.ComputeHash(Encoding.UTF8.GetBytes(password));
        return Convert.ToBase64String(bytes);
    }
}
