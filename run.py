from app import create_app, db
from app.models import User, Store, CommonMedicine, StoreMedicineBatch, Supplier, Customer, Invoice, InvoiceItem

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Store': Store, 'CommonMedicine': CommonMedicine, 'StoreMedicineBatch': StoreMedicineBatch, 'Supplier': Supplier, 'Customer': Customer, 'Invoice': Invoice, 'InvoiceItem': InvoiceItem}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
