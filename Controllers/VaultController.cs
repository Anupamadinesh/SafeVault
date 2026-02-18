using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using SafeVault.Data;

namespace SafeVault.Controllers;

[ApiController]
[Route("api/vault")]
public class VaultController : ControllerBase
{
    private readonly AppDbContext _context;

    public VaultController(AppDbContext context)
    {
        _context = context;
    }

    // Only users with Admin role can access this endpoint
    [Authorize(Roles = "Admin")]
    [HttpGet]
    public IActionResult GetSecrets()
    {
        var secrets = _context.VaultItems.ToList();

        if (!secrets.Any())
            return NotFound("No vault data available.");

        return Ok(secrets);
    }
}
