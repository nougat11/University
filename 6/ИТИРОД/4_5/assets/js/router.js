import Utils from './Utils.js'
import headerView from './views/header.js'
import bannerView from './views/bannerView.js'
import footerView from './views/footer.js'
import register from './views/register.js'
import login from './views/login.js'
import aside from './views/aside.js'
import playlists from './views/playlists.js'
import player from './views/player.js'
import profile from './views/profile.js'
import createPlaylist from './views/createPlaylist.js'
import playlist from './views/playlist.js'
import createSong from './views/createSong.js'
import search from './views/search.js'
import genre from './views/genre.js'
import addSong from './views/addSong.js'
import lyrics from './views/lyrics.js'
import library from './views/library.js'
import editSong from './views/editSong.js'
import editPlaylist from './views/editPlaylist.js'
const routes = {
    '/': headerView,
    '/register': register,
    '/login': login,
    '/profile': profile,
    '/cp': createPlaylist,
    '/playlist/id': playlist,
    '/genre/id': genre,
    '/cs': createSong,
    '/search': search,
    '/addSong': addSong,
    '/lyrics': lyrics,
    '/library': library,
    '/editSong': editSong,
    '/editPlaylist': editPlaylist
};
const router = async() => {
    let request = Utils.parseRequestURL();
    if (request.id !== undefined) {
        request.resource += '/id';
    }
    const footer = document.getElementById('footer');
    footer.style.cssText = "";

    var l = document.styleSheets;
    // Lazy load view element:
    if (request.resource === "") {
        var user = localStorage.getItem('currentUserId');

        if (user === null) {
            const main = document.getElementById('body');
            if (main.classList.contains('main-player')) {
                main.classList.remove('main-player');
            }

            const menu = document.getElementById('menu');
            menu.style.cssText = "display: none";
            var header = document.getElementById('header');
            if (header === null) {
                var tag = document.createElement("header");
                tag.id = "header";

                main.insertAdjacentElement('afterbegin', tag);
            }
            header = document.getElementById('header');
            if (header !== null) {
                header.innerHTML = await headerView.render();
            }
            header.style.cssText = "";
            const root = document.getElementById('root');
            if (root.classList.contains('player-main')) {
                root.classList.remove('player-main');
            }
            if (!root.classList.contains('banner')) {
                root.classList.add('banner');
            }
            const footer = document.getElementById('footer');
            if (footer.classList.contains('footer-player')) {
                footer.classList.remove('footer-player');
            }
            root.innerHTML = await bannerView.render();



            footer.innerHTML = await footerView.render();
        } else {
            const header = document.getElementById('header');
            if (header !== null) {
                header.remove();
            }

            const main = document.getElementById('body');
            if (!main.classList.contains('main-player')) {
                main.classList.add('main-player');
            }
            const menu = document.getElementById('menu');

            menu.style.cssText = "";
            menu.innerHTML = await aside.render();
            await aside.after_render();
            const root = document.getElementById('root');
            if (!root.classList.contains('player-main')) {
                root.classList.add('player-main');
            }
            root.innerHTML = await playlists.render();
            const footer = document.getElementById('footer');
            footer.innerHTML = await player.render();
            await player.after_render();
            if (!footer.classList.contains('footer-player')) {
                footer.classList.add('footer-player');
            }
            if (footer.classList.contains('hide')) {
                footer.classList.remove('hide');
            }


            await playlists.after_render();
        }
    } else {
        const root = document.getElementById('root');
        if (request.resource == "register" || request.resource == "login") {
            if (root.classList.contains('banner')) {
                root.classList.remove('banner');
            }
            const footer = document.getElementById('footer');
            footer.style.cssText = "display: none";
            const header = null || document.getElementById('header');
            header.style.cssText = "display: none";
            const menu = document.getElementById('menu');
            menu.style.cssText = "display: none";
        } else {
            //if (request.resource == "profile") {
            //const main = null || document.getElementById('body');
            //   main.className = '';
            //}
            const header = null || document.getElementById('header');
            if (header !== null) {
                header.remove();
            }
            const main = document.getElementById('body');
            if (!main.classList.contains('main-player')) {
                main.classList.add('main-player');
            }
            const menu = document.getElementById('menu');
            menu.style.cssText = "";
            menu.innerHTML = await aside.render();
            await aside.after_render();
            if (!root.classList.contains('player-main')) {
                root.classList.add('player-main');
            }
            footer.innerHTML = await player.render();
            await player.after_render();
            if (!footer.classList.contains('footer-player')) {
                footer.classList.add('footer-player');
            }
            if (footer.classList.contains('hide')) {
                footer.classList.remove('hide');
            }




        }

        let page = routes['/' + request.resource];
        var maskcss = "css" + page;

        root.innerHTML = await page.render();
        await page.after_render();

    }

    //const content = null || document.getElementById('page_container');

    // Get the parsed URl from the addressbar
    // let request = Utils.parseRequestURL()

    // Parse the URL and if it has an id part, change it with the string ":id"
    // let parsedURL = (request.resource ? '/' + request.resource : '/') + (request.id ? '/:id' : '') + (request.verb ? '/' + request.verb : '')

    // Get the page from our hash of supported routes.
    // If the parsed URL is not in our list of supported routes, select the 404 page instead
    //  let page = routes[parsedURL] ? routes[parsedURL] : Error404
    //  content.innerHTML = await page.render();
    // await page.after_render();

}
window.addEventListener('hashchange', router);

// Listen on page load:
window.addEventListener('load', router);