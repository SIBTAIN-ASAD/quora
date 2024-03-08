import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from '../components/AuthContext';
import './Dashboard.css';

const Dashboard = () => {
    const { currentUser } = useAuth();
    const [commentData, setCommentData] = useState({
        rating: '',
        comment: '',
        review: '',
        catalog: '',
        comment_type: ''
    });
    const [comments, setComments] = useState([]);

    // Redirect to login page if the user is not logged in
    if (!currentUser) {
        window.location.href = '/login';
    }

    const handleLogout = () => {
        // remove the user from local storage and redirect to the login page
        localStorage.removeItem('user');
        window.location.href = '/login';
    }

    const handleChange = (e) => {
        const { name, value } = e.target;
        setCommentData({
            ...commentData,
            [name]: value
        });
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:8000/api/comment', commentData, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                },
            });
            // Fetch comments again after adding a new comment
            fetchComments();
            // Clear comment input
            setCommentData({
                rating: '',
                comment: '',
                review: '',
                catalog: '',
                comment_type: ''
            });
        } catch (error) {
            console.error('Error adding comment:', error);
        }
    }

    const fetchComments = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/comment', {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                },
            });
            setComments(response.data.user_rating_comment);
        } catch (error) {
            console.error('Error fetching comments:', error);
        }
    }

    useEffect(() => {
        fetchComments();
    }, []);

    const handleRemoveComment = async (id) => {
        try {
            await axios.delete(`http://localhost:8000/api/comment`, {
                headers: {
                    Authorization: `Bearer ${localStorage.getItem('token')}`,
                },
                data: {
                    id : id,
                },
            });

            fetchComments();
        } catch (error) {
            console.error('Error removing comment:', error);
        }
    }

    return (
        <div className="pic2 min-h-screen flex justify-center items-center bg-gradient-to-b from-purple-400 via-pink-500 to-red-500 ">
            <div className="container mx-auto w-1/2 p-4 bg-white rounded-lg shadow-lg text-center relative h-5/6"> {/* Add relative positioning */}
                {currentUser ? (
                    <>
                        <h2 className="text-3xl mt-20 font-bold mb-4 text-gray-900">Hi!
                            <span className="fw-bold text-4xl m-2 text-red-500 ">
                                {currentUser.name}
                            </span>
                        </h2>
                        <div className="user-info border-y-2 p-2 w-72 mx-auto mb-6">
                            <p className="text-gray-800 text-lg animated-text"><strong>Email: </strong> {currentUser.email}</p>
                            <p className="text-gray-800 text-lg ps-0 ms-0 animated-text"><strong>Username: </strong> {currentUser.username}</p>
                            <div className="profile-picture mb-6 absolute top-0 left-1/2 transform -translate-x-1/2"> {/* Add absolute positioning */}
                                {currentUser.profile_picture ? (
                                    <img src={currentUser.profile_picture} alt="Profile" className="-mt-16 rounded-full border-4 border-white" style={{ width: '150px', height: '150px' }} />
                                ) : (
                                    <p className="text-gray-700">No profile picture available</p>
                                )}
                            </div>
                        </div>

                        {/* Add comment form */}
                        <form onSubmit={handleSubmit} className="mt-4 h-auto overflow-auto">
                            <div className="grid grid-cols-2 gap-1">
                                <div className="flex flex-col">
                                    <input type="text" name="rating" id="rating" value={commentData.rating} onChange={handleChange} className="p-2 border border-gray-300 rounded-md text-sm" placeholder="Rating" />
                                </div>
                                <div className="flex flex-col">
                                    <input type="text" name="catalog" id="catalog" value={commentData.catalog} onChange={handleChange} className="p-2 border border-gray-300 rounded-md text-sm" placeholder="Catalog" />
                                </div>
                                <div className="flex flex-col">
                                    <input type="text" name="review" id="review" value={commentData.review} onChange={handleChange} className="p-2 border border-gray-300 rounded-md text-sm" placeholder="Review" />
                                </div>
                                <div className="flex flex-col">
                                    <input type="text" name="comment_type" id="comment_type" value={commentData.comment_type} onChange={handleChange} className="p-2 border border-gray-300 rounded-md text-sm" placeholder="Comment Type" />
                                </div>
                                <div className="flex flex-col">
                                    <textarea name="comment" id="comment" value={commentData.comment} onChange={handleChange} className="p-2 border border-gray-300 rounded-md text-sm" rows="3" placeholder="Comment"></textarea>
                                </div>
                                <button type="submit" className="w-40 h-10 mt-10 bg-slate-500 text-white py-2 px-4 rounded-md hover:bg-slate-600 focus:outline-none text-sm">Add Comment</button>
                            </div>
                        </form>



                        {/* Display comments */}
                        <h3 className="text-xl mt-4 font-semibold ">Comments</h3>
                        <div className="mt-6 h-52 overflow-auto">
                            <div className='p-0 m-0'>
                                {comments.map((comment, index) => (
                                    <div key={index} className="bg-gray-100 rounded-md mb-2">
                                        <div className='flex flex-col justify-start text-left'>
                                            <p className=''>Rating: {comment.rating}</p>
                                            <p className=''>Comment: {comment.comment}</p>
                                            <p className=''>Review: {comment.review}</p>
                                            <p className=''>Catalog: {comment.catalog}</p>
                                            <p className=''>Comment Type: {comment.comment_type}</p>
                                        </div>

                                        <button onClick={() => handleRemoveComment(comment.id)} className="text-red-500 hover:text-red-700">Remove</button>
                                    </div>
                                ))}
                            </div>
                        </div>

                        <button className="bg-red-500 my-4 text-white py-2 px-6 rounded-full hover:bg-red-600 focus:outline-none" onClick={handleLogout}>
                            Logout
                        </button>
                    </>

                ) : (
                    <>
                        <h2 className="text-3xl font-bold mb-4 text-gray-900">Welcome to the Dashboard!</h2>
                        <p className="text-gray-700">Please log in to view this page.</p>
                    </>
                )}
            </div>
        </div>
    );
};

export default Dashboard;
