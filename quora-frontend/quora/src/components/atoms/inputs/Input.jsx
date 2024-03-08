// General Input component for forms

import React from 'react';

const Input = (props) => {
    const { type, name, value, handleChange, placeholder, required, className } = props;

    return (
        <div className="flex flex-col">
            <input
                type={type || 'text'}
                name={name || ''}
                id={name || ''}
                value={value || ''}
                onChange={handleChange}
                className={`p-2 border border-gray-300 rounded-md text-sm ${className || ''}`}
                placeholder={placeholder || ''}
                required={required || false}
            />
        </div>
    );
}

export default Input;
