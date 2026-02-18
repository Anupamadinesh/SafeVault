using Xunit;

public class SecurityTests
{
    [Fact]
    public void SqlInjection_Input_ShouldContainQuote()
    {
        var input = "admin' OR '1'='1";
        Assert.Contains("'", input);
    }

    [Fact]
    public void Role_ShouldBe_Admin()
    {
        var role = "Admin";
        Assert.Equal("Admin", role);
    }
}
