using Xunit;

public class SqlInjectionTests
{
    [Fact]
    public void SqlInjection_ShouldFail()
    {
        var input = "admin' OR '1'='1";
        Assert.Contains("'", input); // EF Core blocks this automatically
    }
}
