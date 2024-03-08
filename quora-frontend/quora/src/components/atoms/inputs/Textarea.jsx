// Generic Textarea component for forms

import React from 'react';

const Textarea = (props) => {

    const { name, value, handleChange, placeholder, className, rows } = props;

    return (
        <div className="flex flex-col">
            <textarea
                name={name}
                value={value || ''}
                onChange={handleChange}
                className={`p-2 border border-gray-300 rounded-md text-sm ${className || ''}`}
                rows={rows || 1}
                placeholder={placeholder || ''}
            ></textarea>
        </div>
    );
};

export default Textarea;
