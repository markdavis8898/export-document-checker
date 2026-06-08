#!/usr/bin/env python3
"""
Export Document Checker — validates completeness of international trade documentation.
"""
import json

REQUIRED_DOCS = {
    "commercial_invoice": "Commercial Invoice",
    "packing_list": "Packing List",
    "bill_of_lading": "Bill of Lading / Airway Bill",
    "certificate_of_origin": "Certificate of Origin",
    "export_declaration": "Export Declaration",
}

class DocumentChecker:
    def __init__(self, destination_country, incoterms="FOB"):
        self.destination = destination_country
        self.incoterms = incoterms
        self.documents = {}
    
    def add_document(self, doc_type, document_id, status="present"):
        self.documents[doc_type] = {"id": document_id, "status": status}
    
    def validate(self):
        missing = []
        for key, name in REQUIRED_DOCS.items():
            if key not in self.documents:
                missing.append(name)
        
        return {
            "destination": self.destination,
            "incoterms": self.incoterms,
            "documents_submitted": len(self.documents),
            "documents_required": len(REQUIRED_DOCS),
            "missing_documents": missing,
            "compliant": len(missing) == 0
        }

if __name__ == "__main__":
    checker = DocumentChecker("Germany", "CIF")
    checker.add_document("commercial_invoice", "INV-2026-001")
    checker.add_document("packing_list", "PL-2026-001")
    checker.add_document("bill_of_lading", "BOL-2026-001")
    result = checker.validate()
    print(json.dumps(result, indent=2))
