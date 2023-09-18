import streamlit as st

# Page title
st.title("Pizza Ordering App")

# Sidebar for user information
st.sidebar.header("User Information")
user_name = st.sidebar.text_input("Your Name")
user_address = st.sidebar.text_area("Delivery Address")

# Pizza selection
st.header("Select Your Pizza")

# Pizza size
pizza_size = st.selectbox("Select Pizza Size", ["Small", "Medium", "Large"])

# Toppings
st.subheader("Toppings (Choose one or more)")
toppings = st.multiselect(
    "Select Toppings",
    ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Peppers", "Olives"],
)

# Quantity
quantity = st.number_input("Quantity", min_value=1, value=1)

# Display order summary
st.subheader("Order Summary")
st.write(f"Name: {user_name}")
st.write(f"Delivery Address: {user_address}")
st.write(f"Pizza Size: {pizza_size}")
st.write(f"Toppings: {', '.join(toppings)}")
st.write(f"Quantity: {quantity}")
total_cost = quantity * (
    10 if pizza_size == "Small" else (12 if pizza_size == "Medium" else 14)
)
st.write(f"Total Cost: ${total_cost}")

# Place order button
if st.button("Place Order"):
    st.success("Your order has been placed!")

