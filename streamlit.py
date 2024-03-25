import streamlit as st
import pandas as pd
import random
import pickle
# import warnings

# warnings.filterwarnings("ignore")

from sklearn.ensemble import GradientBoostingClassifier

# Load the model
model_file = "pickle/model.pkl"
with open(model_file, 'rb') as file:
    model = pickle.load(file)

# Load the CSV file
@st.cache
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    return data

def main():
    st.title("Phishing URL Detection")

    st.write("Choose how you want to input URL features:")
    input_option = st.radio("Select Input Option", ("Random from Dataset", "Provide Own"))

    if input_option == "Random from Dataset":
        st.write("Generate a new random row from the dataset:")
        if st.button("Generate New Random"):
            st.write("Generating new random row from dataset...")
            data = load_data("phishing.csv")
            random_row = data.sample(n=1, random_state=random.randint(0, 1000))
            st.write("Random Row:")
            st.write(random_row)

            # Use the generated random row for prediction
            st.write("Predicting with the generated row:")
            features = random_row.values.tolist()[0][1:-1]  # Exclude first and last columns
            # Convert labels to -1, 0, 1
            features = [int(label) if label != 0 else 0 for label in features]
            prediction = model.predict([features])
            st.write("Predicted class:", prediction[0])
    else:
        st.write("Please enter the following URL features:")
        usingIP = st.selectbox("Using IP", [-1, 0, 1])
        long_url = st.number_input("LongURL", min_value=-1, max_value=1, step=1)
        short_url = st.number_input("ShortURL", min_value=-1, max_value=1, step=1)
        symbol_at = st.number_input("Symbol@", min_value=-1, max_value=1, step=1)
        redirecting = st.selectbox("Redirecting//", [-1, 0, 1])
        prefix_suffix = st.selectbox("PrefixSuffix-", [-1, 0, 1])
        sub_domains = st.number_input("SubDomains", min_value=-1, max_value=1, step=1)
        https = st.selectbox("HTTPS", [-1, 0, 1])
        domain_reg_len = st.number_input("DomainRegLen", min_value=-1, max_value=1, step=1)
        favicon = st.selectbox("Favicon", [-1, 0, 1])
        non_std_port = st.selectbox("NonStdPort", [-1, 0, 1])
        https_domain_url = st.selectbox("HTTPSDomainURL", [-1, 0, 1])
        request_url = st.selectbox("RequestURL", [-1, 0, 1])
        anchor_url = st.selectbox("AnchorURL", [-1, 0, 1])
        links_in_script_tags = st.number_input("LinksInScriptTags", min_value=-1, max_value=1, step=1)
        server_form_handler = st.selectbox("ServerFormHandler", [-1, 0, 1])
        info_email = st.selectbox("InfoEmail", [-1, 0, 1])
        abnormal_url = st.selectbox("AbnormalURL", [-1, 0, 1])
        website_forwarding = st.selectbox("WebsiteForwarding", [-1, 0, 1])
        status_bar_cust = st.selectbox("StatusBarCust", [-1, 0, 1])
        disable_right_click = st.selectbox("DisableRightClick", [-1, 0, 1])
        using_popup_window = st.selectbox("UsingPopupWindow", [-1, 0, 1])
        iframe_redirection = st.selectbox("IframeRedirection", [-1, 0, 1])
        age_of_domain = st.number_input("AgeofDomain", min_value=-1, max_value=1, step=1)
        dns_recording = st.selectbox("DNSRecording", [-1, 0, 1])
        website_traffic = st.number_input("WebsiteTraffic", min_value=-1, max_value=1, step=1)
        page_rank = st.number_input("PageRank", min_value=-1, max_value=1, step=1)
        google_index = st.selectbox("GoogleIndex", [-1, 0, 1])
        links_pointing_to_page = st.number_input("LinksPointingToPage", min_value=-1, max_value=1, step=1)
        stats_report = st.selectbox("StatsReport", [-1, 0, 1])

        features = [usingIP, long_url, short_url, symbol_at, redirecting, prefix_suffix, sub_domains, https,
                    domain_reg_len, favicon, non_std_port, https_domain_url, request_url, anchor_url,
                    links_in_script_tags, server_form_handler, info_email, abnormal_url, website_forwarding,
                    status_bar_cust, disable_right_click, using_popup_window, iframe_redirection, age_of_domain,
                    dns_recording, website_traffic, page_rank, google_index, links_pointing_to_page, stats_report]

        if st.button("Submit"):
            # Make prediction
            prediction = model.predict([features])
            st.write("Predicted class:", prediction[0])

if __name__ == "__main__":
    main()









