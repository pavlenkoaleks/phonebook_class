from view import menu,show_contacts,print_message,input_contact,input_return
import model
from view import text
def start():
   pb=model.PhoneBook('phones.txt')
   while True:
       choice = menu()
       match choice:
           case 1:
                pb.open_file()
                print_message(text.open_successfull)
           case 2:
             pass
           case 3:
                show_contacts(pb)
                
           case 4:
             new = input_contact(text.input_new_contact)
             pb.add_contact(new)
             print_message(text.contact_saved(new.name))
           case 5:
             word = input_return(text.search_word)
             result = pb.search(word)
             show_contacts(result)
           case 6:
             word = input_return(text.search_word)
             result = pb.search(word)
             show_contacts(result)
             index = input_return(text.input_index)
             new = input_contact(text.input_change_contact)
             pb.change(int(index),new)
             old_name =pb[int(index)-1].get('name')
             print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))
           case 7:
             word = input_return(text.search_word)
             result = pb.search(word)
             show_contacts(result)
             index = input_return(text.input_delete)
             deleted_contact = pb[int(index)-1].get('name')
             pb.delete(int(index))
             print_message(text.contact_deleted(deleted_contact))
             pb.change_id()
           case 8:
             break