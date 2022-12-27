
sheetname = {'000':
             'abcauthenticatedtypes`(`AuthenticatedTypeID`,`AuthenticatedType`)',
             '001':
             'abcauthpasswordrules`(`PasswordRuleID`,`PasswordRuleName`,`PasswordMinStrength0to100`,`PasswordHistoryDepth`,`PasswordExpirationDays`,`PasswordExpirationWarningDays`,`PasswordMaxFailedAttemptsBeforeLockout`,`PasswordFailedAttemptLockoutPeriodMinutes`)',
             '002':
             'abcbootstrapcontrol`(`ABCBootStrapControlID`,`UsersLastUpdateUTCTime`,`PPhonesLastUpdateUTCTime`,`ServicesLastUpdateUTCTIme`,`UserCurrentSwitchLastUpdateUTCTime`)',
             '003':
             'abcidentities`(`IdentityID`,`IdentityName`,`IdentityTypeID`,`ServerID`,`DBID`,`Pin`,`SyncState`,`SyncPrevIdentityName`,`TenantId`,`DID`,`Username`,`UserDN`,`PhoneAddr`,`MustChangeGUIPassword`,`LastUpdateUTCTime`)',
             '004':
             'abcidentitytypes`(`IdentityTypeID`,`IdentityTypeName`)',
             '005':
             'abcservicemap`(`ServiceMapID`,`IdentityID`,`ServiceTypeID`,`ServiceID`,`SyncState`,`LastUpdateUTCTime`)',
             '006':
             'abcservices`(`ServiceID`,`ServiceTypeID`,`ServerID`,`ServiceURI`,`DBID`,`RPServiceURI`,`SyncState`,`SyncPrevServiceURI`,`LastUpdateUTCTime`)',
             '007':
             'abcservicetypes`(`ServiceTypeID`,`ServiceType`,`AuthenticatedTypeID`,`AllowDelete`)',
             '008':
             'accountcodes`(`AccountCodeID`,`AccountCode`,`AccountCodeInput`,`AccountName`,`TenantID`,`LastUpdateUTCTime`)',
             '009':
             'accountcodetypes`(`AccountCodeTypeID`,`Description`)',
             '010':
             'adminroleattributes`(`AttributeID`,`AttributeDesc`)',
             '011':
             'adminroleattributessetting`(`SettingID`,`SettingDesc`)',
             '012':
             'adminrolepermissions`(`RoleID`,`AttributeID`,`SettingID`,`LastUpdateUTCTime`)'}


for k, v in sheetname.items():
    if len(v) > 32:
        sname = v.split('(~')[0]
