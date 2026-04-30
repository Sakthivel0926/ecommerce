const API_URL = "http://127.0.0.1:8000/api/products/";

async function fetchProducts() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to fetch products");
        }

        const data = await response.json();

        const container = document.getElementById("productList");
        container.innerHTML = "";

        data.forEach(product => {
            const div = document.createElement("div");
            div.classList.add("product");

            div.innerHTML = `
                <h3>${product.name}</h3>
                <p><b>Price:</b> ₹${product.price}</p>
                <p><b>Stock:</b> ${product.stock}</p>
                <p><b>Category:</b> ${product.category}</p>
                <p>${product.prod_description || ""}</p>
                <button onclick="deleteProduct(${product.id})">Delete</button>
            `;

            container.appendChild(div);
        });

    } catch (error) {
        console.error("Error fetching products:", error);
    }
}

async function deleteProduct(id) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/products/delete/${id}/`, {
            method: "DELETE"
        });

        if (!response.ok) {
            throw new Error("Delete failed");
        }

        fetchProducts(); // refresh list

    } catch (error) {
        console.error("Error deleting product:", error);
    }
}

document.addEventListener("DOMContentLoaded", fetchProducts);