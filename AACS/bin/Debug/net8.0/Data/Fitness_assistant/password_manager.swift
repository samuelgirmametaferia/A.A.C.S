import SwiftUI
import Keychain

struct PasswordItem: Identifiable {
    let id = UUID()
    let name: String
    let password: String
}

class PasswordManager: ObservableObject {
    @Published var passwords: [PasswordItem] = []

    func addPassword(name: String, password: String) {
        let newItem = PasswordItem(name: name, password: password)
        passwords.append(newItem)
        savePassword(password: password, for: name)
    }

    func getPassword(for name: String) -> String? {
        return Keychain.get(key: name)
    }

    func savePassword(password: String, for name: String) {
        Keychain.set(value: password, key: name)
    }
}

struct ContentView: View {
    @StateObject var manager = PasswordManager()

    var body: some View {
        NavigationView {
            List {
                ForEach(manager.passwords) { password in
                    NavigationLink(destination: PasswordDetailView(password: password)) {
                        Text(password.name)
                    }
                }
                .onDelete(perform: deletePassword)
            }
            .navigationTitle("Password Manager")
            .toolbar {
                Button(action: {
                    // Add new password view
                }) {
                    Image(systemName: "plus")
                }
            }
        }
    }

    func deletePassword(at offsets: IndexSet) {
        manager.passwords.remove(atOffsets: offsets)
    }
}

struct PasswordDetailView: View {
    let password: PasswordItem

    var body: some View {
        VStack {
            Text(password.name)
                .font(.title)
            Text(password.password)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}