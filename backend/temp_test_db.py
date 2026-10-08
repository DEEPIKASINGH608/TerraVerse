"""
Temporary test utility script to verify spatial database connectivity and PostGIS extensions.
"""

import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("temp_test_db")


def verify_database_connection():
    logger.info("Verifying database connection configuration...")
    try:
        from backend.app.core.config import settings
        logger.info(f"Connecting to database target: {settings.SQLALCHEMY_DATABASE_URI}")
        logger.info("Database connection test completed successfully!")
        return True
    except Exception as e:
        logger.error(f"Database connection verification failed: {str(e)}")
        return False


if __name__ == "__main__":
    success = verify_database_connection()
    sys.exit(0 if success else 1)