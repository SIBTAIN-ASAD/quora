// Comment component to display a single comment

import React from 'react';

import { DeleteButton } from '../../atoms';

const Comment = (props) => {

    const { comment, onDelete } = props;

    // Get all keys of the comment object
    const commentKeys = Object.keys(comment);

    return (
        <div className="bg-gray-100 rounded-md mb-2 pb-2">
            <div className='flex flex-col justify-start text-left p-4'>
                {commentKeys.map((key, index) => (
                    key !== 'id' && key !== 'user' && key !== 'pk' && (
                        <p key={index} className="flex">
                            <span className="w-40 text-green-900 fw-bold">{key}:</span>
                            <span>{comment[key]}</span>
                        </p>
                    )
                ))}
                <DeleteButton className="border border-red-700 mt-4 w-40 mx-auto rounded hover:bg-red-500 hover:text-white"
                    text="Delete Comment"
                    onClick={() => onDelete(comment.id)} />
            </div>
        </div>
    );
};

export default Comment;
