import streamlit as st

# Create a dictionary to simulate user data
users = {
    "user1": {"name": "John Doe", "balance": 1000},
    "user2": {"name": "Jane Smith", "balance": 1500},
}

# Page title
st.title("Simple Banking App")

# Sidebar for user selection
selected_user = st.sidebar.selectbox("Select User", list(users.keys()))

# Display user's name and balance
st.header(f"Welcome, {users[selected_user]['name']}")
st.write(f"Your current balance is: ${users[selected_user]['balance']:.2f}")

# Banking operations
st.header("Banking Operations")

# Deposit operation
if st.button("Deposit"):
    deposit_amount = st.number_input("Enter deposit amount", min_value=0.01)
    if deposit_amount:
        users[selected_user]['balance'] += deposit_amount
        st.success(f"Deposited ${deposit_amount:.2f} successfully.")

# Withdraw operation
if st.button("Withdraw"):
    withdraw_amount = st.number_input("Enter withdrawal amount", min_value=0.01)
    if withdraw_amount:
        if withdraw_amount <= users[selected_user]['balance']:
            users[selected_user]['balance'] -= withdraw_amount
            st.success(f"Withdrew ${withdraw_amount:.2f} successfully.")
        else:
            st.error("Insufficient balance for withdrawal.")

# Transfer operation
if st.button("Transfer"):
    recipient_user = st.selectbox("Select recipient", list(users.keys()))
    transfer_amount = st.number_input("Enter transfer amount", min_value=0.01)
    if transfer_amount:
        if transfer_amount <= users[selected_user]['balance']:
            users[selected_user]['balance'] -= transfer_amount
            users[recipient_user]['balance'] += transfer_amount
            st.success(f"Transferred ${transfer_amount:.2f} to {users[recipient_user]['name']} successfully.")
        else:
            st.error("Insufficient balance for transfer.")

# Display user balance after transactions
st.subheader("Updated Balance")
st.write(f"Your updated balance is: ${users[selected_user]['balance']:.2f}")
