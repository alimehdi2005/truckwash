import streamlit as st
from streamlit_option_menu import option_menu


def local_html(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_html("style/style.css")



st.title('_GM Commercial_ _Cleaning_')

selected = option_menu(
     menu_title=None,
     options=["BOOK NOW", "CONTACT US"],
    icons=["pencil-fill", "telephone_receiver"],
    orientation="horizontal",)



#book now section

if selected == "BOOK NOW":

    st.header("Book your truck wash today!")
    st.markdown("After filling out this form please check your email to conform or reschedule your appointment")

    booking = """   
      <div class="container">
      <form target="_blank" action="https://formsubmit.co/alixbox5@outlook.com" method="POST">
        <div class="form-group">
          <div class="form-row">
            <div class="col">
              <input type="text" name="name" class="form-control" placeholder="Name / Company Name" required>
            </div>
            <div class="col">
              <input type="email" name="email" class="form-control" placeholder="Email Address" required>
              <input type="number" name="num" class="form-control" placeholder="Number of Trucks" required>
              <div class="col">
              <input type="tel" name="tel" class="form-control" placeholder="Phone Number" required>
            <input type="datetime-local" name="date" class="form-control" placeholder="Date and Time" required>
            </div>
          </div>
        </div>
        <div class="form-group">
        </div>
        <button type="submit" class="btn btn-lg btn-dark btn-block">Submit Form</button>
      </form>
    </div>
    """
    st.markdown(booking, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

 #contact us from

if selected == "CONTACT US":

  st.header("Get In Touch With Us")
  st.markdown("Please fill out this form to reach out to our support staff")

  contact = """
     <div class="container">
      <form target="_blank" action="https://formsubmit.co/alixbox5@outlook.com" method="POST">
        <div class="form-group">
          <div class="form-row">
            <div class="col">
              <input type="text" name="name" class="form-control" placeholder="Name / Company Name" required>
            </div>
            <div class="col">
              <input type="email" name="email" class="form-control" placeholder="Email Address" required>
              <div class="col">
              <input type="tel" name="tel" class="form-control" placeholder="Phone Number" required>
            </div>
          </div>
        </div>
        <div class="form-group">
          <textarea placeholder="Your Message" class="form-control" name="message" rows="10" required></textarea>
        </div>
        <button type="submit" class="btn btn-lg btn-dark btn-block">Submit Form</button>
      </form>
    </div>
    """
  st.markdown(contact, unsafe_allow_html=True)




def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
