import React, { Component } from 'react'

export default class Header extends Component {
    render() {
        return (
            <div id="sidenav-bar" className="sidenav font-mono">
                <br/><br/>
                <a href="/" className="sidebar-item">Home</a>
                <a href="/search" className="sidebar-item">Search</a>
                <hr/>
                <a href="/files/my-drive" className="sidebar-item">My Drive</a>
                <a href="/shared_drives" className="sidebar-item">Shared Drives</a>
                <hr/>
                <a href="/files/shared-with-me" className="sidebar-item">Shared With Me</a>
                <a href="/files/favourites" className="sidebar-item">Favourites</a>
                <hr/>
                <a href="/settings" className="sidebar-item">Settings</a>
            </div>
        )
    }
}
