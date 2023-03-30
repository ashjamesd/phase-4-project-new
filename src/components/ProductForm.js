import React, { useState } from 'react';

const ProductForm = ({ onAddProduct }) => {
  const [imageUrl, setImageUrl] = useState('');
  const [name, setName] = useState('');
  const [price, setPrice] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const newProduct = { imageUrl, name, price };
    onAddProduct(newProduct);
    setImageUrl('');
    setName('');
    setPrice('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Image URL:
        <input type="text" value={imageUrl} onChange={(e) => setImageUrl(e.target.value)} />
      </label>
      <label>
        Name:
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
      </label>
      <label>
        Price:
        <input type="text" value={price} onChange={(e) => setPrice(e.target.value)} />
      </label>
      <button type="submit">Add Product</button>
    </form>
  );
};

export default ProductForm;
