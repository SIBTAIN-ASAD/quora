// User info item component

import React from 'react';

const UserInfoItem = (props) => {
    const { label, value } = props;

    return (
        <p className="text-gray-800 text-lg animated-text">
            <strong>{label}: </strong> {value}
        </p>
    );
}

export default UserInfoItem;
