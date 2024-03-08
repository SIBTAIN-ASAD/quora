// AppIcon component

import React from 'react';
import logo from '../../../assets/images/logo-short.png';

const AppIcon = () => {
    return (
        <div className="text-center">
            <a href="/profile"><img src={logo} alt="logo" className="mx-auto my-10" width="100px" /></a>
        </div>
    );
}

export default AppIcon;
