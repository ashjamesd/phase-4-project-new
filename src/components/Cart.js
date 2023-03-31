import React from 'react';

const Cart = ({ cartItems }) => {
  return (
    <div className='cart'>
      <h2>Cart</h2>
      {cartItems && cartItems.map(item => (
        <div key={item.id}>
          <h3>{item.name}</h3>
          <p>${item.price}</p>
          {/* <button className='removeItem'>Remove from cart</button> */}
        </div>
      ))}
    </div>
  );
};

export default Cart;
