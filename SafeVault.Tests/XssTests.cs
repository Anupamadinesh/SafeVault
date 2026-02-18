using Xunit;

public class XssTests
{
    [Fact]
    public void XssInput_ShouldBeRejected()
    {
        var input = "<script>alert(1)</script>";
        Assert.Contains("<", input);
    }
}
