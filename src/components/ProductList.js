import React from 'react';

const ProductList = ({ products, onAddToCart }) => {
  return (
    <div>
      <h2>Featured Products</h2>
      {products.map((product) => (
        <div key={product.id}>
          <img src={product.imageUrl} alt={product.name} />
          <h3>{product.name}</h3>
          <p>{product.price}</p>
          <button onClick ={()=>onAddToCart(product)}>Add to Cart</button>

        </div>
      ))}
    </div>
  );
};

export default ProductList;
