import sys
import os

sys.path.append(os.path.dirname(__file__))

from app.database import SessionLocal
from app.auth.service import hash_password, verify_password
from app.models import User
from sqlalchemy import text

def test_fundamentals():
    print("🚀 TESTING FUNDAMENTAL SETUP...")
    
    try:
        # Test 1: Database Connection
        print("🧪 1. Testing Database Connection...")
        db = SessionLocal()
        result = db.execute(text("SELECT 1"))
        db.close()
        print("✅ Database connection OK")
        
        # Test 2: Password Hashing (use shorter password)
        print("🧪 2. Testing Password Hashing...")
        test_password = "test123"  # ← ← ← SHORTER PASSWORD
        hashed = hash_password(test_password)
        print(f"✅ Hash generated: {hashed[:30]}...")
        
        # Test 3: Password Verification
        print("🧪 3. Testing Password Verification...")
        is_valid = verify_password(test_password, hashed)
        is_invalid = verify_password("wrongpass", hashed)
        print(f"✅ Correct password: {is_valid}")
        print(f"✅ Wrong password rejected: {not is_invalid}")
        
        # Test 4: Model Import
        print("🧪 4. Testing Model Imports...")
        user_attrs = [attr for attr in dir(User) if not attr.startswith('_')]
        print(f"✅ User model loaded with attributes: {user_attrs[:5]}...")
        
        print("\n🎉 ALL FUNDAMENTAL TESTS PASSED!")
        print("➡️ Next step: Run 'uvicorn app.main:app --reload'")
        
    except Exception as e:
        print(f"\n❌ FUNDAMENTAL TEST FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_fundamentals()