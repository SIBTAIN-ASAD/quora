// Delete button component

import React from 'react';

const DeleteButton = (props) => {

    const { onClick , className} = props;

    return (
        <button onClick={onClick} className={`text-red-500 hover:text-red-700 ${className || ''}`}>
            Remove
        </button>
    );
};

export default DeleteButton;
