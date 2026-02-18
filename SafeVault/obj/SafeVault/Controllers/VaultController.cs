using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using SafeVault.Data;

namespace SafeVault.Controllers
{
    [ApiController]
    [Route("api/vault")]
    public class VaultController : ControllerBase
    {
        private readonly AppDbContext _context;

        public VaultController(AppDbContext context)
        {
            _context = context;
        }

        // Only ADMIN users can access this endpoint
        [Authorize(Roles = "Admin")]
        [HttpGet]
        public IActionResult GetSecrets()
        {
            var data = _context.VaultItems.ToList();
            return Ok(data);
        }
    }
}
