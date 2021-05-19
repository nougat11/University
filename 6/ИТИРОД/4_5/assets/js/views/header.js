let headerView = {
    render: async() => {
        let view =
            `
            <div class="header-container">
            <a class="Homelink" href="#">Home</a>
            <nav>
                <a class="reg" href="/#/register">Register</a>
                <a class="reg" href="/#/login">Login</a>
            </nav>
            </div>
            `
        return view
    }

}
export default headerView;